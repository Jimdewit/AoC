# Jim de Wit's Advent of Code repository.

## Rudimentary puzzle downloader 
./get_puzzle.py can be used to download the daily puzzle input, and will automatically spawn
a browser window with the puzzle for the day. Note that it requires a json-formatted file
that contains the AoC session cookie (this is used by AoC to make sure every user gets their
own individual puzzle).

The cookie can be found by opening any daily input and inspecting the headers that were sent
along with the GET request for that page. In the cookies header, there is a bit that reads
```session=365.....536```. The script expects this value to be in a json-formatted file:

```{"session": "365...536" }``` The location and filename can be passed to the script as a
command line argument.

**Since this cookie is personal, do make sure to add the cookie file to $GIT_DIR/info/exclude,
so it doesn't end up in a public repository!**