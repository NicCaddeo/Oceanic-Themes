import os
import subprocess
import sys
import shutil

EXTENSION_NAME = "oceanic-themes"
VSIX_NAME = f"{EXTENSION_NAME}.vsix"
PACKAGE_JSON = "package.json"

repo_path = os.path.dirname(os.path.abspath(__file__))


def replace_extension_name(new_name):
    pkg_path = os.path.join(repo_path, PACKAGE_JSON)
    with open(pkg_path, "r") as f:
        content = f.read()
    if EXTENSION_NAME in content:
        content = content.replace(EXTENSION_NAME, new_name)
        with open(pkg_path, "w") as f:
            f.write(content)
        print(f"Replaced extension name with {new_name} in package.json.")
    else:
        print("No replacement needed in package.json.")


def package_and_install():
    print("Packaging extension...")
    subprocess.run(["vsce", "package"], check=True)
    vsix_files = [f for f in os.listdir(repo_path) if f.endswith(".vsix")]
    if not vsix_files:
        print("No VSIX file found. Packaging may have failed.")
        sys.exit(1)
    vsix_file = vsix_files[0]
    print(f"Installing {vsix_file} to VS Code...")
    subprocess.run(["code", "--install-extension", vsix_file], check=True)
    print("Extension installed successfully.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        new_name = sys.argv[1]
        replace_extension_name(new_name)
    package_and_install()
