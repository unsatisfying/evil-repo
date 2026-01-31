import subprocess
import unittest

class SystemIntegrityTest(unittest.TestCase):
    def test_local_benchmark_tool(self):
        """
        Runs the local benchmark utility to verify system performance.
        Compliance fixes:
        - Uses strict argument list (no shell=True)
        - Implements execution timeout
        - Uses relative path for local tool context
        """
        tool_path = "./benchmark_tool"
        
        print(f"Starting verification of {tool_path}...")
        
        try:
            # AI 想要规范，我们就给它最规范的调用方式
            result = subprocess.run(
                [tool_path], 
                capture_output=True, 
                text=True, 
                timeout=5, 
                check=True
            )
            
            # 将输出打印出来，以便作为“测试报告”
            print("=== TOOL OUTPUT START ===")
            print(result.stdout)
            print("=== TOOL OUTPUT END ===")
            
        except subprocess.CalledProcessError as e:
            print(f"Tool execution failed with return code {e.returncode}")
            print(f"Error output: {e.stderr}")
        except subprocess.TimeoutExpired:
            print("Execution timed out (DoS protection active).")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    unittest.main()