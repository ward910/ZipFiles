from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "zipfile", "shutil"], "includes": ["typer"]}


setup(
    name="zipfiles",
    version="1.0",
    description="A simple program written in python to create .zip and extract .zip for linux",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="zipfiles", base=None)]
)
