import subprocess, os, distro

def gpuc():
    comand = "lspci | grep -E 'VGA|3D'"
    prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = prompt.communicate()[0].decode("utf-8")
    linect = output.count("\n")
    pkname = output.split("\n")
    if "NVIDIA" not in output:
        return False
    else:
        if linect == 1:
            supprt = "single"
        else:
            supprt = "optims"
        jsondt = {
            "supprt": supprt,
            "gpuqnt": linect,
            "gpulst": pkname,
        }
        return jsondt

def main():
    jsondt = {
        "System": str(os.uname().sysname) + " v" + str(os.uname().release),
        "Hostname": str(os.uname().nodename),
        "Version": str(os.uname().version),
        "Distribution": str(distro.os_release_info()["name"]) + " " + str(
            distro.os_release_info()["version_id"]) + " " + str(os.uname().machine),
    }
    return jsondt

def avbl():
    if str(distro.os_release_info()["name"]) == "Fedora":
        if int(distro.os_release_info()["version_id"]) >= 32:
            return "full"
        else:
            return "half"
    else:
        return False

if __name__ == "__main__":
    main()