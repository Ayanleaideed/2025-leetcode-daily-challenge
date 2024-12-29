import os
import sys
import shutil
import logging
import time
import subprocess
from pathlib import Path
from typing import Optional
import git
from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv
import tempfile
import uuid

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

class GitHubAISolution:
    """
    LeetCode solution manager with improved Windows compatibility.
    """
    
    def __init__(self):
        """Initialize with Windows-friendly directory handling."""
        self.repo_url = "https://github.com/Ayanleaideed/2025-leetcode-daily-challenge"
        self.base_dir = self._get_safe_directory()
        self.local_path = self._prepare_directory()
        self.repo = None
        self._load_environment()

    def _get_safe_directory(self) -> str:
        """Get a safe directory path that avoids Windows permission issues."""
        # Use temp directory as base to avoid permission issues
        temp_base = tempfile.gettempdir()
        unique_id = str(uuid.uuid4())[:8]
        safe_dir = os.path.join(temp_base, f"leetcode_solutions_{unique_id}")
        return safe_dir

    def _prepare_directory(self) -> str:
        """Prepare a clean directory with proper Windows permissions."""
        try:
            # Create new directory
            os.makedirs(self.base_dir, exist_ok=True)
            
            # Copy current directory contents if needed
            current_dir = os.getcwd()
            target_dir = os.path.join(self.base_dir, "workspace")
            
            if os.path.exists(target_dir):
                # Use system commands for forced removal on Windows
                if sys.platform == "win32":
                    subprocess.run(['cmd', '/c', 'rmdir', '/s', '/q', target_dir], 
                                 check=False, capture_output=True)
                else:
                    shutil.rmtree(target_dir, ignore_errors=True)
            
            os.makedirs(target_dir, exist_ok=True)
            logger.info(f"Working directory: {target_dir}")
            return target_dir
            
        except Exception as e:
            logger.error(f"Directory preparation failed: {e}")
            raise

    def _load_environment(self):
        """Set up OpenAI client."""
        try:
            load_dotenv()
            self.api_key = os.getenv("OPENAI_API_KEY")
            
            if not self.api_key:
                self.api_key = input("Enter your OpenAI API key: ").strip()
                if not self.api_key:
                    raise ValueError("OpenAI API key is required")
                
                env_path = os.path.expanduser('~/.leetcode_env')
                with open(env_path, 'w') as f:
                    f.write(f"OPENAI_API_KEY={self.api_key}")
            
            self.client = OpenAI(api_key=self.api_key)
        except Exception as e:
            logger.error(f"Environment setup failed: {e}")
            raise

    def setup_repository(self) -> None:
        """Set up repository with Windows compatibility."""
        try:
            logger.info(f"Setting up repository in: {self.local_path}")
            
            # Force clean clone
            if sys.platform == "win32":
                subprocess.run(['cmd', '/c', 'rmdir', '/s', '/q', 
                              os.path.join(self.local_path, '.git')],
                             check=False, capture_output=True)
            
            # Fresh clone
            self.repo = git.Repo.clone_from(self.repo_url, self.local_path)
            
            # Configure Git
            with self.repo.config_writer() as git_config:
                git_config.set_value('user', 'name', 'LeetCode Bot')
                git_config.set_value('user', 'email', 'leetcode@example.com')
                git_config.set_value('core', 'autocrlf', 'true')
                git_config.set_value('core', 'fileMode', 'false')
            
        except Exception as e:
            logger.error(f"Repository setup failed: {str(e)}")
            raise

    def generate_random_problem(self) -> tuple[str, str]:
        """Generate a random LeetCode-style problem."""
        try:
            prompt = """Generate a random LeetCode-style problem. Return only in this format:
Problem Name: [name]
Description: [description]

Make it a unique algorithmic problem."""
            
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a LeetCode problem generator."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            content = response.choices[0].message.content
            lines = content.split('\n')
            problem_name = lines[0].replace('Problem Name:', '').strip()
            description = '\n'.join(lines[2:]).strip()
            
            return problem_name, description
                
        except Exception as e:
            logger.error(f"Problem generation failed: {e}")
            raise

    def generate_solution(self, problem_description: str) -> str:
        """Generate solution with clean code format."""
        try:
            prompt = f"""
Generate a clean Python solution for: {problem_description}

Return ONLY this format:
'''
Problem Description:
[Brief description]

Solution Approach:
[Core algorithm explanation]

Complexity Analysis:
- Time: O(?)
- Space: O(?)
'''

def solution_function(parameters):
    \"\"\"
    [Function description]
    Args: [parameters description]
    Returns: [return value description]
    \"\"\"
    # Implementation
"""
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a senior developer creating production-ready LeetCode solutions."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"Solution generation failed: {e}")
            raise

    def save_solution(self, code: str, problem_name: str) -> str:
        """Save solution with proper file handling."""
        try:
            solutions_dir = os.path.join(self.local_path, 'solutions')
            os.makedirs(solutions_dir, exist_ok=True)
            
            date_str = datetime.now().strftime('%Y%m%d')
            safe_name = "".join(c for c in problem_name if c.isalnum() or c.isspace())
            safe_name = safe_name.replace(' ', '_').lower()
            
            file_path = os.path.join(solutions_dir, f"{date_str}_{safe_name}.py")
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(code)
            
            # Copy to current directory
            current_dir_path = os.path.join(os.getcwd(), 'solutions')
            os.makedirs(current_dir_path, exist_ok=True)
            shutil.copy2(file_path, current_dir_path)
            
            logger.info(f"Solution saved: {file_path}")
            logger.info(f"Solution copied to: {current_dir_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"Failed to save solution: {e}")
            raise

    def commit_and_push(self, problem_name: str) -> None:
        """Commit and push with retry logic."""
        try:
            self.repo.git.add(A=True)
            commit_msg = f"Add solution: {problem_name}"
            
            for attempt in range(3):  # Retry up to 3 times
                try:
                    self.repo.index.commit(commit_msg)
                    self.repo.git.push('origin', 'main')
                    break
                except git.GitCommandError as e:
                    if attempt == 2:  # Last attempt
                        raise
                    time.sleep(2)  # Wait before retry
                    
            logger.info(f"Changes pushed to: {self.repo_url}")
            
        except Exception as e:
            logger.error(f"Push failed: {e}")
            raise

def main():
    """Main execution flow with multiple problems."""
    try:
        solution_gen = GitHubAISolution()
        
        logger.info("Setting up repository...")
        solution_gen.setup_repository()
        
        num_problems = 5
        logger.info(f"Generating {num_problems} problems...")
        
        for i in range(num_problems):
            try:
                if i > 0:
                    logger.info("Cooling down for 10 seconds...")
                    time.sleep(10)
                
                logger.info(f"\n🔄 Problem {i+1}/{num_problems}")
                
                # Generate and solve
                problem_name, problem_desc = solution_gen.generate_random_problem()
                logger.info(f"Generated: {problem_name}")
                
                logger.info("Generating solution...")
                solution_code = solution_gen.generate_solution(problem_desc)
                
                logger.info("Saving solution...")
                file_path = solution_gen.save_solution(solution_code, problem_name)
                
                logger.info("Pushing changes...")
                solution_gen.commit_and_push(problem_name)
                
                logger.info(f"✅ Completed problem {i+1}: {problem_name}")
                
            except Exception as e:
                logger.error(f"Failed problem {i+1}: {e}")
                continue
        
        logger.info("\n🎉 All problems completed!")
        print("\nSolutions are in both the 'solutions' directory and your current directory")
        
    except KeyboardInterrupt:
        logger.info("\nProcess interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Process failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()


'''
Problem Description:
The task is to calculate the minimum total time required to transport all passengers in an intelligent elevator system. The elevator moves at a speed of one floor per second, and people take 1 second to board or exit the elevator. Multiple people can board or exit concurrently.

Solution Approach:
The problem can be solved using a greedy approach. We first sort the list of passengers based on their start floors. Then, for each passenger in the sorted list, if the elevator is currently above the passenger's start floor, it travels down to that floor in |current - start| seconds. If the elevator is currently below the start floor, it travels to that floor in the same amount of time. The passenger then boards the elevator, taking 1 second. Finally, the elevator takes the passenger to their destination floor in |start - end| seconds.

The time complexity of this solution is determined by the sorting operation. In Python, the `sorted` function uses a variant of the Timsort algorithm whose worst-case time complexity is O(n log n). Therefore, the overall time complexity of this solution is O(n log n).

The space complexity of this solution is O(n), arising from the storage of the passenger list.

---

def minElevatorTime(n, passengers):
    """
    Function to calculate the minimum total time to transport all passengers in an intelligent elevator system.
    Args: 
    - n: An integer representing the number of floors.
    - passengers: A list of lists, where each inner list contains two integers representing the start and end floors of a passenger.
    
    Returns: 
    - An integer representing the minimum total time to transport all passengers.
    """

    # Sort the passengers based on their start floors
    passengers = sorted(passengers)

    total_time = 0
    current_floor = 0

    for passenger in passengers:
        start, end = passenger

        # Elevator travels to the start floor
        total_time += abs(current_floor - start) 

        # Passenger boards the elevator
        total_time += 1 

        # Elevator travels to the end floor
        total_time += abs(start - end) 

        # Passenger exits the elevator
        total_time += 1

        # Update the current floor of the elevator
        current_floor = end 

    return total_time
'''
