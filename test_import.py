import sys
print("Python exe:", sys.executable)
print("sys.path:")
for p in sys.path:
    print("  ", p)

try:
    import sklearn
    print("scikit-learn version:", sklearn.__version__)
    print("sklearn module at:", sklearn.__file__)
except Exception as e:
    print("ERROR importing sklearn:", e)