''' Main script of the program '''
import cv2

from window import find_window_hwnds, find_rect, focus_window, NoWindowFoundError
from screen import screenshot
from settings import WINDOW_TITLE


def main():
    ''' Main function of the script '''
    try:
        hwnds = find_window_hwnds(WINDOW_TITLE)
        focus_window(hwnds[1])
        rect = find_rect(hwnds[1])
        img = screenshot(rect)
        cv2.imshow(WINDOW_TITLE, img)
        cv2.waitKey()
    except NoWindowFoundError:
        print('No window detected')


if __name__ == '__main__':
    main()
