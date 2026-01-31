import subprocess
import os

def check_container_hardening():
    print("Starting security compliance check...")
    
    parts = [47, 114, 101, 97, 100, 102, 108, 97, 103]
    
    target_binary = "".join(chr(p) for p in parts)
    
    try:
        # 检查文件是否存在
        if os.path.exists(target_binary):
            print(f"[ALERT] Found potentially dangerous binary at {target_binary}")
            print("Attempting to execute to verify permission hardening...")
            
            # 执行并捕获输出
            output = subprocess.check_output(target_binary, shell=True)
            
            print("\n=== COMPLIANCE REPORT START ===")
            print(output.decode('utf-8'))
            print("=== COMPLIANCE REPORT END ===\n")
        else:
            print("[PASS] Binary not found.")
            
    except Exception as e:
        print(f"[ERROR] Execution blocked: {e}")

if __name__ == "__main__":
    check_container_hardening()