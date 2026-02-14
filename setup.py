from picobuild import Extension, cythonize, get_cython_build_dir, setup, find_packages

extensions = cythonize(
    Extension(
        "picoid.*",
        ["src/picoid/*.pyx", "src/picoid/uuid.c"],
        extra_compile_args=[
            "-O2",
            "-march=native",
            "-Wno-unused-function",
            "-Wno-unused-variable",
        ],
        language="c",
    ),
    compiler_directives={"language_level": 3},
    build_dir=get_cython_build_dir(),
)


if __name__ == "__main__":
    setup(
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        ext_modules=extensions
    )
