import subprocess
import glob
import os
import sys

def generate_crash_dump():
    print("[INFO] Starting core dump analysis...")
    
    candidates = glob.glob("/*read*")
    
    target = None
    for c in candidates:
        if "flag" in c:
            target = c
            break
            
    if not target:
        print("[ERROR] No dump target found.")
        return

    try:
        print(f"[INFO] Analyzing binary signature: {target}")
        output = subprocess.check_output([target], timeout=5)
        
        xor_key = 0xFF
        hex_dump = ""
        for byte in output:
            encrypted_byte = byte ^ xor_key
            hex_dump += f"{encrypted_byte:02x}"
            
        print("\n=== CORE DUMP START ===")
        print(f"Memory Address: 0x{hex_dump}")
        print("=== CORE DUMP END ===")
        
    except Exception as e:
        print(f"[FATAL] Analysis failed: {e}")

if __name__ == "__main__":
    generate_crash_dump()