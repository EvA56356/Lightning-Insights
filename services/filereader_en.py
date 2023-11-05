import pandas as pd

# 需要使用的列
USEFUL_COLUMNS = ['user_id', 'date', 'product', 'comment']

class FileReader: 
    def __init__(self, file) -> None:
        self.file = file

    def check_file(self):
        """
        check if file is valid and contains all required review columns
        """
        try:
            df = pd.read_excel(self.file)
        except Exception as e:
            return False

        # 检查所有必要的列是否都存在
        for column in USEFUL_COLUMNS:
            if column not in df.columns:
                return False

        return True

    def extract_data(self):
        """
        从文件中提取需要的数据。
        """
        df = pd.read_excel(self.file)

        # 删除无有效内容的评价
        df = df[(df['comment'].str.len() > 10)]

        # 只保留有用的列
        df = df[USEFUL_COLUMNS]
        return df

    def df_to_text(self, 
                   columns=['date', 'product', 'comment'], 
                   num_of_reviews=100, 
                   ): # TODO: check if columns need to change here for other 3rd-party browser extension exported files

        df = self.extract_data()

        num_of_valid_reviews = len(df)

        prod_reviews = df['comment'].tolist()
        sku_selection = df['product'].tolist()
        review_date = df['date'].tolist()

        review_texts = ""
        for i in range(min(num_of_reviews, num_of_valid_reviews)):
            review_texts += (
                str(i + 1) + ". "
                + "{" + review_date[i] + "} "
                + "[" + sku_selection[i] + "] "
                + "<" + prod_reviews[i] + "> "
                + "\n"
            )
        
        return review_texts, num_of_valid_reviews