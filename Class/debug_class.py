import logging

def init_logger_for_class(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # ハンドラが登録されていなかったら登録
    if not logger.hasHandlers():
    # sh = logging.StreamHandler(sys.stdout)
        sh = logging.StreamHandler()
        sh.setLevel(level)

        # フォーマッタを定義する（第一引数はメッセージのフォーマット文字列、第二引数は日付時刻のフォーマット文字列）
        fmt = logging.Formatter("%(asctime)s [%(name)s] [%(levelname)s] %(filename)s/%(funcName)s - %(message)s", "%m-%d%H:%M:%S")

        # フォーマッタをハンドラに紐づける
        sh.setFormatter(fmt)
        logger.addHandler(sh)

    # ログ出力
    logger.debug("Start debug.")

    return logger