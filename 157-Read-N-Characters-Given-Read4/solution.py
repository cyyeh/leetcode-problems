"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        # 記錄目前已讀幾個字
        current_char = 0
        
        # 初始化read4函式所需的buf4
        buf4 = [' '] * 4
        
        # 如果目前已讀字數超過可讀字數n，跳出迴圈
        while current_char < n:
            buf4_num_char = read4(buf4)
            # 如果加上buf4所含字數超過n，則僅最多讀取至第n個字
            if buf4_num_char + current_char > n:
                buf[current_char:n] = buf4[:n-current_char]
                current_char = n
            else:
                buf[current_char:current_char+buf4_num_char] = buf4[:buf4_num_char]
                current_char += buf4_num_char
            
            # 表示已讀完所有文字
            if buf4_num_char < 4:
                break
