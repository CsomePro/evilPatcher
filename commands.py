import subprocess

def getoutput(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output = process.communicate()[0]
    # print(output.strip())
    return output.strip()

if __name__ == "__main__":
    print(getoutput("seccomp-tools asm ./sandboxs/mini_sandbox.asm  -a i386 -f inspect"))
