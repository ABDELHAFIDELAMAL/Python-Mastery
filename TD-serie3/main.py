def convertNumberToText(n: int) -> str:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    if n == 0:
        return "zero"

    if n < 0:
        return "minus " + convertNumberToText(-n)

    # Basic words
    units = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen")
    tens = ("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
    scales = (
        (10**12, "trillion"),
        (10**9,  "billion"),
        (10**6,  "million"),
        (10**3,  "thousand"),
        (1,      "")
    )

    def _below_thousand(num: int) -> str:
        """Convert a number from 0..999 to words (no leading/trailing spaces)."""
        parts = []
        if num >= 100:
            h = num // 100
            parts.append(units[h])
            parts.append("hundred")
            num = num % 100
            if num:
                # optional connector "and" could be added for British English:
                # parts.append("and")
                pass
        if num >= 20:
            t = num // 10
            parts.append(tens[t])
            r = num % 10
            if r:
                parts.append(units[r])
        elif num > 0:
            parts.append(units[num])
        return " ".join(parts)

    words = []
    remainder = n
    for scale_value, scale_name in scales:
        if remainder >= scale_value:
            if scale_value == 1:
                # final small chunk (<1000)
                chunk = remainder
            else:
                chunk = remainder // scale_value
            # break chunk into below-thousand pieces if needed (since scale_value may be > 1000)
            if scale_value >= 1000:
                # chunk may be > 999 (e.g., for billions we want chunk like 1..999)
                # so we recursively convert chunk (which is <= 999 for typical splits if scales defined as above).
                chunk_words = convertNumberToText(chunk)  # recursion is safe because chunk < n
                words.append(chunk_words)
            else:
                # scale_value == 1: chunk is the remainder itself (<1000 typically)
                words.append(_below_thousand(chunk))
            if scale_name:
                words.append(scale_name)
            remainder = remainder % scale_value
    # join and clean up multiple spaces
    result = " ".join(w for w in words if w).strip()
    # normalize multiple spaces (shouldn't be necessary but safe)
    result = " ".join(result.split())
    return result

number = int(input("Enter a number: "))
print(convertNumberToText(number))