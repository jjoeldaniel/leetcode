class Solution:

    def is_digit_log(self, log: str):
        word = log.split(' ')[1]

        for i in word:
            if i.isalpha():
                return False
        return True

    def custom_sort_key(self, logs):
        words = logs.split(' ', 1)
        return (words[1], words[0])

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []

        for i in logs:
            if self.is_digit_log(i):
                digit_logs.append(i)
            else:
                letter_logs.append(i)

        return sorted(letter_logs, key=self.custom_sort_key)+digit_logs
