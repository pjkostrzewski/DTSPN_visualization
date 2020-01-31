from helpers import *
from InputView import InputView
from AnimationView import AnimationView


def main():
    try:
        InputView().run()
        run_dtspn_exe(f"{build_path}", "dtspn.exe")
        AnimationView().run()
    except Exception as e:
        print(e)
        raise Exception("something went wrong")
    finally:
        remove_files(f"{build_path}/DTSPN_input.txt", f"{build_path}/DubinsPath.txt")


if __name__ == '__main__':
    main()
    pygame.quit()
