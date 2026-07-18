from ai_studio.core import Kernel


def main():
    kernel = Kernel()
    try:
        kernel.boot()
        # TODO: создать QApplication и MainWindow
    finally:
        kernel.shutdown()


if __name__ == "__main__":
    main()