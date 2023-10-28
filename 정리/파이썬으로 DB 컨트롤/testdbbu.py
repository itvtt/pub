import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import pymysql
from datetime import timedelta, datetime
from tkinter import filedialog
import csv


class DatabaseViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Viewer")
        self.root.geometry("2000x900")  # UI 크기 설정

        self.init_ui()
        self.setup_database()
        self.current_table = "data"  # 기본 테이블 설정
        self.load_data(self.current_table)  # 기본 테이블 데이터 로드
        self.treeview.bind("<Control-a>", self.select_all_items)

    def select_all_items(self, event):
        for item in self.treeview.get_children():
            self.treeview.selection_add(item)

    def init_ui(self):
        self.date_label = tk.Label(self.root, text="Search by Date:")
        self.start_date_input = DateEntry(self.root, date_pattern="yyyy/mm/dd", show_time=True)
        self.end_date_input = DateEntry(self.root, date_pattern="yyyy/mm/dd", show_time=True)

        self.value_label = tk.Label(self.root, text="Search by Value:")
        self.value_input = ttk.Entry(self.root)
        
        # 새로운 검색 입력창들 추가
        self.eqpid_label = tk.Label(self.root, text="Search by Eqpid:")
        self.eqpid_input = ttk.Entry(self.root)

        self.foupid_label = tk.Label(self.root, text="Search by Foupid:")
        self.foupid_input = ttk.Entry(self.root)

        self.lotid_label = tk.Label(self.root, text="Search by Lotid:")
        self.lotid_input = ttk.Entry(self.root)

        # 검색 버튼 추가
        self.search_button = tk.Button(self.root, text="Search", command=self.search_data, width=15, height=2, bg="blue", fg="white", font=("Arial", 12))
        # width: 버튼의 너비, bg: 배경 색상, fg: 글자 색상
        
        # 버튼 추가
        self.button_data = tk.Button(self.root, text="Data", command=lambda: self.load_data("data"), width=15, height=2, bg="blue", fg="white", font=("Arial", 12))
        self.button_data1 = tk.Button(self.root, text="Data1", command=lambda: self.load_data("data1"), width=15, height=2, bg="blue", fg="white", font=("Arial", 12))
        self.button_data2 = tk.Button(self.root, text="Data2", command=lambda: self.load_data("data2"), width=15, height=2, bg="blue", fg="white", font=("Arial", 12))
        self.button_data3 = tk.Button(self.root, text="Data3", command=lambda: self.load_data("data3"), width=15, height=2, bg="blue", fg="white", font=("Arial", 12))
        self.button_data4 = tk.Button(self.root, text="Data4", command=lambda: self.load_data("data4"), width=15, height=2, bg="blue", fg="white", font=("Arial", 12))

        
        self.treeview = ttk.Treeview(self.root, show="headings")
        self.treeview.place(x=10, y=180, width=780, height=300)  # 좌표와 크기 설정
        self.treeview.bind("<Configure>", self.adjust_treeview_columns)  # Treeview 너비에 따라 열 너비 자동 조절


        # 버튼들을 상단에 위치시키고 나머지 UI 요소들을 조정
        self.button_data.place(x=10, y=10)  # 상단에 위치
        self.button_data1.place(x=200, y=10)  # 상단에 위치
        self.button_data2.place(x=400, y=10)  # 상단에 위치
        self.button_data3.place(x=600, y=10)  # 상단에 위치
        self.button_data4.place(x=800, y=10)  # 상단에 위치

        # 다른 UI 요소들을 버튼들 아래로 내림
        self.date_label.place(x=10, y=70)
        self.start_date_input.place(x=120, y=70)
        self.end_date_input.place(x=240, y=70)
        self.eqpid_label.place(x=10, y=100)
        self.eqpid_input.place(x=120, y=100)
        self.foupid_label.place(x=10, y=130)
        self.foupid_input.place(x=120, y=130)
        self.lotid_label.place(x=10, y=160)
        self.lotid_input.place(x=120, y=160)
        self.value_label.place(x=10, y=190)
        self.value_input.place(x=120, y=190)
        self.search_button.place(x=300, y=130)

        self.treeview.place(x=10, y=220, width=1980, height=700)
        self.treeview.bind("<Configure>", self.adjust_treeview_columns)


         # 추가한 버튼
        self.export_button = tk.Button(self.root, text="Export CSV", command=self.export_csv, width=15, height=2, bg="green", fg="white", font=("Arial", 12))
        self.export_button.place(x=450, y=130)



    def setup_database(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',
            database='testdb'
        )
        self.cursor = self.connection.cursor()

        for i in range(5):
            self.cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS data{i} (
                    date DATETIME,
                    value TEXT,
                    eqpid TEXT,
                    foupid TEXT,
                    lotid TEXT
                )
            """)
            self.connection.commit()

    def load_data(self, table_name):
        self.current_table = table_name  # 선택된 테이블 정보 저장
        self.start_date_input.set_date(datetime.now())  # 시작 날짜 초기화
        self.end_date_input.set_date(datetime.now())  # 종료 날짜 초기화
        self.value_input.delete(0, "end")  # Value 검색 입력창 초기화
        self.eqpid_input.delete(0, "end")  # Eqpid 검색 입력창 초기화
        self.foupid_input.delete(0, "end")  # Foupid 검색 입력창 초기화
        self.lotid_input.delete(0, "end")  # Lotid 검색 입력창 초기화

        self.treeview.delete(*self.treeview.get_children())

        self.cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = [column[0] for column in self.cursor.fetchall()]
        self.treeview["columns"] = columns

        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=100)

        # 어제와 오늘 날짜 범위 설정
        today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")

        query = f"SELECT * FROM {table_name} WHERE date BETWEEN %s AND %s"
        self.cursor.execute(query, (yesterday, today))
        data = self.cursor.fetchall()

        for row in data:
            self.treeview.insert("", "end", values=row)

    def search_data(self):
        start_date = self.start_date_input.get_date()
        end_date = self.end_date_input.get_date() + timedelta(days=1)

        value_query = self.value_input.get()
        eqpid_query = self.eqpid_input.get()
        foupid_query = self.foupid_input.get()
        lotid_query = self.lotid_input.get()

        table_name = self.current_table

        self.treeview.delete(*self.treeview.get_children())

        query = f"""
            SELECT * FROM {table_name}
            WHERE date >= %s AND date < %s
        """
        query_params = [start_date.strftime("%Y-%m-%d %H:%M:%S"), end_date.strftime("%Y-%m-%d %H:%M:%S")]

        if value_query:
            query += " AND value LIKE %s"
            query_params.append(f"%{value_query}%")

        if eqpid_query:
            query += " AND eqpid LIKE %s"
            query_params.append(f"%{eqpid_query}%")

        if foupid_query:
            query += " AND foupid LIKE %s"
            query_params.append(f"%{foupid_query}%")

        if lotid_query:
            query += " AND lotid LIKE %s"
            query_params.append(f"%{lotid_query}%")

        self.cursor.execute(query, tuple(query_params))
        data = self.cursor.fetchall()

        for row in data:
            self.treeview.insert("", "end", values=row)

    def adjust_treeview_height(self, event):
        self.treeview_height = event.height // 30  # 30은 예상 아이템 높이
        self.treeview.config(height=self.treeview_height)


    def adjust_treeview_columns(self, event):
        # 열 너비 자동 조절
        for col in self.treeview["columns"]:
            if self.current_table == "data" and col == "additional_column":  # data의 추가 컬럼에 대한 조건 처리
                self.treeview.column(col, width=int(self.treeview.winfo_width()/6), anchor="center")  # 6은 열의 개수
            elif self.current_table == "data1" and col == "additional_column":  # data의 추가 컬럼에 대한 조건 처리
                self.treeview.column(col, width=int(self.treeview.winfo_width()/6), anchor="center")  # 6은 열의 개수    
            elif self.current_table == "data2" and col == "additional_column":  # data의 추가 컬럼에 대한 조건 처리
                self.treeview.column(col, width=int(self.treeview.winfo_width()/6), anchor="center")  # 6은 열의 개수
            elif self.current_table == "data3" and col == "additional_column":  # data의 추가 컬럼에 대한 조건 처리
                self.treeview.column(col, width=int(self.treeview.winfo_width()/6), anchor="center")  # 6은 열의 개수    
            elif self.current_table == "data4" and col == "additional_column":  # data의 추가 컬럼에 대한 조건 처리
                self.treeview.column(col, width=int(self.treeview.winfo_width()/6), anchor="center")  # 6은 열의 개수
            else:
                self.treeview.column(col, width=int(self.treeview.winfo_width()/5), anchor="center")  # 5는 열의 개수

    def export_csv(self):
        selected_items = self.treeview.selection()  # 선택된 아이템 가져오기
        if not selected_items:
            return  # 선택된 아이템이 없으면 함수 종료

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return  # 파일 경로가 없으면 함수 종료

        selected_data = []
        for item in selected_items:
            selected_data.append(self.treeview.item(item, "values"))

        with open(file_path, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            # 열 이름 기록
            column_names = [self.treeview.heading(col, "text") for col in self.treeview["columns"]]
            csv_writer.writerow(column_names)
            # 데이터 기록
            for row in selected_data:
                csv_writer.writerow(row)



if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseViewer(root)
    root.lift()
    root.mainloop()