import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        # Check for custom delimiter(s)
        delimiters = [',', '\n']
        custom_delim_match = re.match(r'^//(\[.*\]|.)\n(.*)', numbers, re.DOTALL)

        if custom_delim_match:
            delim_part = custom_delim_match.group(1)
            numbers = custom_delim_match.group(2)

            # Handle delimiters with []
            if delim_part.startswith('[') and delim_part.endswith(']'):
                # Extract all delimiters inside []
                delimiters = re.findall(r'\[(.*?)\]', delim_part)
            else:
                delimiters = [delim_part]

        # Build regex to split by all delimiters
        split_pattern = '|'.join(map(re.escape, delimiters))
        num_list = re.split(split_pattern, numbers)

        # Convert to int and filter empty strings
        int_list = []
        negatives = []
        for n in num_list:
            if n == '':
                continue
            val = int(n)
            if val < 0:
                negatives.append(val)
            elif val <= 1000:
                int_list.append(val)

        if negatives:
            raise Exception(f"negatives not allowed {negatives}")

        return sum(int_list)
