#!/usr/bin/env python3

import csv
import os

def print_greeting():
    """挨拶メッセージを表示する"""
    print("Hello, Tadashi!")
    print("-" * 30)

def read_and_display_csv(file_path):
    """CSVファイルを読み取り整形して表示する"""
    if not os.path.exists(file_path):
        print(f"エラー: ファイル {file_path} が見つかりません。")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            # ヘッダーを取得
            headers = next(reader)
            
            # ヘッダーを表示
            print("CSVデータの表示:")
            
            # 各カラムの最大幅を計算（ヘッダーと値の両方を考慮）
            col_widths = [len(h) for h in headers]
            
            # 一度すべての行を読み込んで最大幅を計算
            rows = list(reader)
            for row in rows:
                for i, cell in enumerate(row):
                    if i < len(col_widths):
                        col_widths[i] = max(col_widths[i], len(cell))
            
            # ヘッダー行を出力
            header_format = " | ".join(["{:<" + str(width) + "}" for width in col_widths])
            print(header_format.format(*headers))
            
            # 区切り線を出力
            print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))
            
            # データ行を出力
            for row in rows:
                print(header_format.format(*row))
                
    except Exception as e:
        print(f"エラー: CSVファイルの読み込み中に問題が発生しました: {e}")

def main():
    """メイン関数"""
    # 挨拶を表示
    print_greeting()
    
    # カレントディレクトリのCSVファイルを読み取り表示
    csv_path = "sample_data.csv"
    read_and_display_csv(csv_path)

if __name__ == "__main__":
    main()
