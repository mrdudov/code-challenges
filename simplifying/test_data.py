test_data = [    
    {
        "equalities": ["a + a = b", "b - d = c", "a + b = d"],
        "formula": "c + a + b",
        "answer": "2a",
    },
    {
        "equalities": ["a + 3g = k", "-70a = g"], 
        "formula": "-k + a", 
        "answer": "210a",
    },
    {
        "equalities": ["-j -j -j + j = b"], 
        "formula": "-j - b", 
        "answer": "1j",
    },
    {
        "equalities": ['(-3f + q) + r = l', '4f + q = r', '-10f = q'],
        "formula": "20l + 20(q - 200f)",
        "answer": "-4580f",
    },
    {
        "equalities":  ['-(-(-(-(-(g))))) - l  = h', '8l = g'],
        "formula": "h - l - g",
        "answer": "-18l",
    },
    {    
        "equalities": ['x = b', 'b = c', 'c = d', 'd = e'],
        "formula": "c",
        "answer": "1x",
    },
    {
        "equalities": ['y + 6Y - k - 6 K = f', ' F + k + Y - y = K', 'Y = k', 'y = Y', 'y + Y = F'],
        "formula":"k - f + y",
        "answer":"14y",
    },
    {
        "equalities": ['-0s = j', '2s = Y', '4s + 5Y = i'],
        "formula": "1(-3Y + 5(4j + 2i + 3j)) - 3Y + 1i",
        "answer": "142s",
    },
    {
        "equalities": ['2A = y', '4A + 3y = i', 'A - 0y + 5i = a', '8A + i - 5a = J', '-6A - 3i - 4a + 3J = N', '-5A - 7y + 4J + 8N = O'],
        "formula": "-4y + 4(4i - 3(1(5O + 4i) + 3i) + 2(-4i + 5a - 2a)) + 4a + 2J - 2N + 4O",
        "answer": "482048A",
    },
    {
        "equalities": ['5X = q', '-1X + 1q = e', '1X + 7q - 0e = U', '5X - 7q + 9e + 3U = H', '-X + 6q - 2e + 7H = O', 'X + 6q + 8e + U - 2H + 9O = z'],
        "formula": "4(2z - 2O - 2e) + 2e + 4U + 5H + 3z",
        "answer": "73800X",
    },
    {
        "equalities": ['-5X = B', '0X + 3B = I', '9X - 7B + 3I = h', '-5X + 5B + 5I + 4h = Z', '-2X + 3B - 7I - 8h = D'],
        "formula": "4B + 2I + 3h - 4Z + 3D",
        "answer": "671X",
    },
    {
        "equalities": ['-8o = R', '-0o - 6R = l', '7o = g', '5o + 7R + 6l + 3g = U', '2o + R + 4l + 6g - 5U = m', '4o + R + 5l - 6g + 3U + 5m = V'],
        "formula": "2R - 3l + 1(3l + 2(-3V + 3l + 1U) - 2(5g - 4l)) + 1m",
        "answer": "26092o",
    },
    {

        "equalities": ['-2G = r', '-4G + 9r = J', '1G - 5r - 2J = n', '-6G + 5r + 9J = f'],
        "formula": "2(-3f + 2f) - 3J + 5(1n - 4r + 1J) - 4f",
        "answer": "1555G",
    },
    {
        "equalities": ['-6w = q', '8w + 2q = h', '-6w + 9q + 4h = a'],
        "formula": "-1q + 3(5h + 2h + 1q) + 5a",
        "answer": "-476w",
    },
    {
        "equalities": ['-9A = U', '-9A + 9U = o', '-6A + 2U + o = z'],
        "formula": "-1U + 5o + 3z",
        "answer": "-783A",
    },
    {
        "equalities": ['6o = l', '3o + 6l = g', '-5o + 7g = Q', '3o + 9g - 2Q = h', '2o - 7l + 5g + 7Q = b', '9o + 8l + 5Q + 2h + 0b = k'],
        "formula": "1(-4l + 4(-1b + 5Q) - 3b) - 2g - 2Q - 4h - 4b - 4(5k - 3(3(3l + 5h) - 1Q - 3k) - 2Q)",
        "answer": "-107923o",
    },
    {
        "equalities": ['7p = L', '-4p + 2L = f', '-3p - 5L + 2f = k'],
        "formula": "5f - 4k",
        "answer": "122p",
    },
    {
        "equalities": ['-2X = Y', '-6X + 4Y = s', '-6X + 2Y + 6s = m', '9X - 4s = n', '-5X + 3s + 7m + n = O', '-9X - 5Y - 9s + 4m + 3n + O = D'],
        "formula": "4Y + 4(-2O + 3O) + 2(-2n - 3(4n + 2Y + 4s) + 3s) - 2(4Y - 1n)",
        "answer": "-3966X",
    },
    {
        "equalities": ['1G = y', '5G + 6y = U', '-7G + 5y = a', '8G - 5y = b', '-4G + 7y + 1b = f'],
        "formula": "2y - 2(-4(1a - 4f + 1U) - 1f) + 4(2(1a + 4a + 1a) + 5y) - 1b + 1f",
        "answer": "-179G",
    },
    {
        "equalities": ['6q = Y', '-3q + 4Y = a', '-q - 7Y - 7a = N', '-4q + 7Y - 0a = f'],
        "formula": "-2Y + 1a + 2(5N - 4f) - 1f",
        "answer": "-2233q",
    },
    {
        "equalities": ['9X = x', '8X - 0x = e', '4X + 8x + 7e = U', '-4X - x = w', '-8X - 8x + 7e - 0w = P'],
        "formula": "3e + 1U - 1(5w + 5e) - 3P",
        "answer": "253X",
    },
    {
        "equalities": ['-7W = c', '5W + 4c = P', '-7W + 8c = n', '5W + 3c + 7P + 8n = O', '-8W + 4c + 3P - n + 2O = S'],
        "formula": "-2c - 1P + 5n + 5(1c - 4O) - 3(2S + 1(1S - 3(3c + 5S - 2S)) - 3O)",
        "answer": "-18283W",
    },
    {
        "equalities": ['-3X = K', '2X + 4K = e', '0X + 7K + 7e = P', 'X - 7K - 9P = z', '-X + 4K - 5e + 9P - z = V', '7X + 0K - 5e + 0P + 3z - 6V = S'],
        "formula": "2K - 3e + 4P + 3z - 2V - 1S",
        "answer": "-6889X",
    },
    {
        "equalities": ['1d = R', '3d + 2R = G', '7d - 4R + 6G = A', '5d + 8R + 7G + 2A = l', 'd + 7R - G + 5A + 5l = T'],
        "formula": "-2R + 4(-3l + 4T) - 3A + 2T",
        "answer": "11815d",
    },
    {
        "equalities": ['0X = c', '-9X + 8c = r', '8X + 1c + 4r = J', '-1X + 2c + 3J = V', '-9X - 9c + 9r + 3J + 5V = E'],
        "formula": "4c - 2r + 5J - 2V - 4E",
        "answer": "2444X",
    },
    {
        "equalities": ['-2C = q', '-3C - 7q = M', '4C + M = Z'],
        "formula": "-1(5Z + 5Z - 4Z) + 4Z",
        "answer": "-30C",
    },
    {
        "equalities": ['8t = B', '-2t + 0B = W', '4t + 5B = r', '-1t + 7B + 6r = z', '-t - 7B + 7r + 7z = b'],
        "formula": "-1(-1r + 4W) - 4(-4b + 1B - 1W) + 4r - 1z + 2b",
        "answer": "44581t",
    },
    {
        "equalities": ['-7Y = W', '9Y + 1W = L', '6Y - 0W = i', '-Y + 5L = r', '-2Y + i + 5r = m', '-2Y + 8W + L + 3r - 0m = Z'],
        "formula": "1W + 3L - 4(5m + 1Z - 1m) + 3r - 3m + 1(4(-2W - 1m - 2i) - 3L)",
        "answer": "-983Y",
    },
    {
        "equalities": ['4o = W', '4o + 3W = l', '8o - 6W + 3l = f', '3o + 6W + 1l + 5f = u', '-7o + 0W + 8l - 5f = C'],
        "formula": "-3W - 3l - 2f - 4u + 3C",
        "answer": "-1053o",
    },
    {
        "equalities": ['-1q = u', '5q = i', '-q + 4u + 5i = r', '-5q - 9u - 8i = n', '-6q - u - 6i + 3r + 1n = S'],
        "formula": "-1r + 2(3S - 4(1i + 1u)) + 4S",
        "answer": "-162q",
    },
    {
        "equalities": ['-2x = y', '-5x + 2y = w', '-1x + 4y + 4w = N', '8x - 3N = f'],
        "formula": "2y - 4w - 4N + 4f",
        "answer": "784x",
    },
    {
        "equalities": ['4U = H', '-4U + 4H = J', 'U - 4J = z', '3U + 6H + 4J - 8z = f'],
        "formula": "3H - 1J + 1(-3f - 2H) + 3f",
        "answer": "-8U",
    },
    {
        "equalities": ['-2q = R', '4q = Q', '-q - 0R + 7Q = P', '6q - 7R + 0Q + 5P = Z'],
        "formula": "-3(-1(5Z - 1Q) + 3R) + 4Q - 1P + 3Z",
        "answer": "2785q",
    },
    {
        "equalities": ['-4Y = K', '4Y + 3K = y', '-4Y + 7K = U', '-5Y - 7K + 6y + 7U = j', 'Y + 3y + 9U + 1j = N', '4Y + 2U - 2j + 4N = C'],
        "formula": "-1K + 5y - 3(5U - 1(2j + 1U - 3K)) + 2(2N - 4y + 1(3U - 4C + 3j)) + 1N + 2C",
        "answer": "5280Y",
    },
    {
        "equalities": ['3t = c', '2t + 3c = L', '1t + 8c + 8L = P', '4t + c - L - 4P = V'],
        "formula": "5c - 1L + 4P + 5(-4P + 5V)",
        "answer": "-13204t",
    },
    {
        "equalities": ['-4t = l', '5t + 3l = I', '3t + 6l - 0I = b', '0t + 4l + 2I - 8b = F'],
        "formula": "1l + 4(1b - 4b) + 2F",
        "answer": "524t",
    },
    {
        "equalities": ['-4o = I', '-5o = N', '5o - 7I - 7N = z'],
        "formula": "-3(5z + 5z) - 4z",
        "answer": "-2312o",
    },
    {
        "equalities": ['-3o = Y', '-8o - 9Y = A', '-4o - 6Y + 3A = M', '-o - 3Y - 5A = e', '-8o + 5A - 5M + 3e = N', '1o + 9Y + 8A + 6e + 2N = z'],
        "formula": "3Y + 1A + 1M - 3e - 4z",
        "answer": "6158o",
    },
    {
        "equalities": ['-7x = q', '-5x + 5q = I', '-5x + 1q + I = a'],
        "formula": "-1q + 2I",
        "answer": "-73x",
    },
    {
        "equalities": ['B = c', '6B = M', '-3B + 6c + 4M = W', '9B + 7c - 2M + 7W = u', '5B - 0W + 8u = k'],
        "formula": "3c - 2M - 3W - 1u + 2k",
        "answer": "2815B",
    },
    {
        "equalities": ['3v = e', '5v - 3e = j', '-5v + 2e + 8j = D', '-3v - 0e - j + 3D = k'],
        "formula": "-4(-2k - 4k + 3k) - 2(4k - 1k - 3j) - 3k",
        "answer": "-300v",
    },
    {
        "equalities": ['0f = q', '-5f + 4q = Y', '5f - q + 6Y = z'],
        "formula": "-3Y + 4z",
        "answer": "-85f",
    },
    {
        "equalities": ['2d = Q', '-0d + 8Q = P', '-5d - 8Q + 4P = N', '-8d - 8Q + 7P - N = h', '-3d + 8Q + 5P - N = Z', '8d + 2P - 2N = k'],
        "formula": "4Q - 1P - 1N - 1h - 2Z + 2(5P - 4k + 2P)",
        "answer": "396d",
    },
    {
        "equalities": ['-8v = c', '2v = Q', 'v - 7c + 9Q = j', '1v - c + 7Q + 4j = n'],
        "formula": "-2c + 2Q",
        "answer": "20v",
    },
    {
        "equalities": ['8q = v', '-6q = A', '-6q - 7A = g', '-1q - 8v + 4A = i', '3q - 7v - 7g - 2i = a', '8q + 8v - 3g + 9i + 8a = T'],
        "formula": "-2v - 3A - 1g - 3i - 4(-3T - 4(-4A + 1T + 5g) + 1g) + 1T",
        "answer": "-50384q",
    },
    {
        "equalities": ['8f = V', '4f - 4V = L', '2f - 3V + 8L = e'],
        "formula": "3V",
        "answer": "24f",
    },
    {
        "equalities": ['3q = K', '-5q + 8K = Q', '-9q + 8K = H', '-5q - 9K + 3Q + 7H = s', '0q + 6K + 5Q + 8H + 8s = n', '-2q + 4Q + 9H + 9s - 4n = F'],
        "formula": "-1(-1H - 2n) + 2(4H - 3(2H + 3Q) - 1n) + 2H + 5s + 3n + 4F",
        "answer": "-10740q",
    },
    {
        "equalities": ['-2u = r', '9u + 4r = f', '-3u + 2r - 6f = S', '-7u + 3r + 9f - 3S = C'],
        "formula": "-4r - 4f + 5(-4(4f - 2f + 1r) + 5(1f - 3C) + 3r) - 1C",
        "answer": "-2661u",
    },
    {
        "equalities": ['2p = L', '-5p + L = a', '-p + 7a = j', '-5p + 1L + 6j = N', '-8p - 5L + 9j + 8N = D'],
        "formula": "3L + 1a + 3(1(4D - 1j - 4a) + 1(-3a - 4N) + 1(5N + 2(3D - 3D) + 5D)) - 2N + 1(5L + 4j)",
        "answer": "-35073p",
    },
    {
        "equalities": ['-7p = M', '-4p - 9M = Q', '-9p = a', '-1p + M + 6Q + 2a = r'],
        "formula": "-1(-4a - 3a - 4Q) + 1Q + 1a + 5(-1Q + 2(2Q + 2r + 3a) - 1a)",
        "answer": "7443p",
    },
    {
        "equalities": ['-5W = c', '5W + 4c = a', '5W - 0a = z', '-3W - c + 5a + 8z = T'],
        "formula": "-3(2T - 1(-4T + 2T)) + 1(4z - 2T) + 2z + 5T",
        "answer": "327W",
    },
    {
        "equalities": ['-4t = u', '-3t + 1u = K', '2t - 4u + 1K = a'],
        "formula": "4u + 5K + 2a",
        "answer": "-29t",
    },
    {
        "equalities": ['-0c = L', '-2c + 8L = T', '8c + 5T = w', '0c - 0T + 2w = F'],
        "formula": "3L + 3T - 1(-1F + 4L) - 3F",
        "answer": "2c",
    },
    {
        "equalities": ['-5B = l', '4B = g', '-0B - 3l = R'],
        "formula": "-3l - 1(5(3g + 3l) + 1l) + 5R",
        "answer": "110B",
    },
    {
        "equalities": ['-0d = M', '-3d + 1M = R', '-6d + M + 5R = b'],
        "formula": "5M - 2(-1R + 2(2M + 3R + 3R) - 3b) + 1b",
        "answer": "-81d",
    },
    {
        "equalities": ['-7d = w', '9d = j', '0d - w - j = H'],
        "formula": "-3(5H - 2j + 2w) + 3(5(3w - 2H - 2H) - 4w + 1H) + 5(5H + 4w)",
        "answer": "-181d",
    },
    {
        "equalities": ['-3q = g', '-6q - 5g = i', '0q + 2g + 5i = r', '-3q + 9g + 8i + 7r = N', '-5q - 4g + 9i + 2r + 8N = z', '-2q + 3g - 3i + 7r + 9N + z = f'],
        "formula": "-4g + 5i + 2r + 1z - 4f",
        "answer": "-20203q",
    },
    {
        "equalities": ['-q = v', '-6q + 8v = J', '7q + 8v = r', '3q - 8v + 3J - 4r = j', '5q + 8v - 3J - 6r = F', '-5q - 8v - 8J - 7r + 7j - F = u'],
        "formula": "4v + 3J + 5r + 3j + 1u",
        "answer": "-244q",
    },
    {
        "equalities": ['-1Y = M', '-7Y - 8M = l', '4Y - 8M = H', '-4Y + 2M + 7l - 8H = F'],
        "formula": "4(5(2(-2M - 4F + 5F) + 4l) + 1H + 4F) - 2l + 4H + 5F",
        "answer": "-5541Y",
    },
    {
        "equalities": ['-6P = l', '-0P + 0l = g', '9P + 7l + 3g = i'],
        "formula": "3l - 3(-4(-4l - 2i - 3l) + 5i) - 4(1(3l + 5i + 4g) - 2i)",
        "answer": "2241P",
    },
    {
        "equalities": ['4H = V', '-6H + 7V = u', '-8H + 3V - 3u = g'],
        "formula": "-1(5u - 3V + 5g) - 4(5g - 1g)",
        "answer": "1204H",
    },
    {
        "equalities": ['1Y = B', '-0Y - 9B = W', '-8Y - B - 6W = V', '-2Y + 5B = A', '-6Y + 2B - A = D'],
        "formula": "3B - 1W + 1(-4B - 4V) + 1A + 4D",
        "answer": "-197Y",
    },
    {
        "equalities": ['8g = Q', '-g - 5Q = i', '-7g - 4Q = w', '2g + 8Q - 6i = N', '4g + Q + 4i + 2w + 2N = h'],
        "formula": "-4Q + 1i + 4w + 1(-1Q - 3Q - 2i) - 3h",
        "answer": "-1361g",
    }
]
