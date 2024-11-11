def decode_message( s: str, p: str) -> bool:

# write your code here
        const m = message.length;
    const p = pattern.length;

    const dp = Array(m + 1).fill(false).map(() => Array(p + 1).fill(false));

    dp[0][0] = true;

    for (let j = 1; j <= p; j++) {
        if (pattern[j - 1] === '*') {
            dp[0][j] = dp[0][j - 1];
        }
    }
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= p; j++) {
            if (pattern[j - 1] === '*') {
                dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
            } else if (pattern[j - 1] === '?' || pattern[j - 1] === message[i - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = false;
            }
        }
    }

    return dp[m][p];

  
        return False