def decode_message( s: str, p: str) -> bool:

        m = len(message)
    p = len(pattern)

    # Create a DP table where dp[i][j] is True if pattern[0..j-1] matches message[0..i-1]
    dp = [[False] * (p + 1) for _ in range(m + 1)]

    # Base case: empty pattern matches empty message
    dp[0][0] = True

    # Initialize DP table for patterns that start with '*'
    for j in range(1, p + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, p + 1):
            if pattern[j - 1] == '*':
                # '*' can match zero or more characters
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif pattern[j - 1] == '?' or pattern[j - 1] == message[i - 1]:
                # '?' matches any single character, or exact match of characters
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = False

    return dp[m][p]



  
        # return False