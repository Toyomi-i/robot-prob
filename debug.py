import logging 
import sys

DEBUG_PRINT = True
# DEBUG_PRINT = False

def init_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(level)

    # フォーマッタを定義する（第一引数はメッセージのフォーマット文字列、第二引数は日付時刻のフォーマット文字列）
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(filename)s/%(funcName)s - %(message)s", "%m-%d%H:%M:%S")

    # フォーマッタをハンドラに紐づける
    sh.setFormatter(fmt)
    logger.addHandler(sh)

    # ログ出力
    logger.debug("Start debug.")

    return logger

def debug_print_onestep(elems: list):
    if DEBUG_PRINT:        
        for e in elems:
            print(f"elems: {e}")
    return