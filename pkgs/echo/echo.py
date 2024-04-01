def echo_help():
    print("echo повторяет всё что вы скажете")
def echo_ver():
    print("echo 0.01, поставляется с wiSHpy")
def echo(*ctx):
    print(' '.join(ctx))