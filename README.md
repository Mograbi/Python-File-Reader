# Python-File-Reader
File Reader class for python
you can easily read text file with this simplified file reader class.

example:
```
  fr = FileReader("D:\\tmp.txt")
  line = fr.next_line()
  while not fr.EOF():
	  # TODO: write your code here
	  line = fr.next_line()

  fr.close()
```
