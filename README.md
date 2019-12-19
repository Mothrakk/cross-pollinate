# cross-pollinate

Self-bot script to seek out people you share mutual servers with.

Beware that self-bots are technically not allowed and you might get in trouble for using one.

## Usage

Put your user token into `token.txt` and run `main.py`. The output will get exported to a new `mutuals.json` file.

### Specifying arguments

You can pass guilds as arguments into the script, seperated by semicolons. This filters the output, such that it will filter out mutuals that are not in every guild specified. For example, the following Powershell query will only return mutuals that are in both `Kenshi Community Discord` and `The Programmer's Hangout`:

```python.exe .\main.py Kenshi Community Discord`;The Programmer`'s Hangout```

(The backticks are there to escape Powershell formatting.)

**How to get your user token:**

1. open discord client
2. ctrl + shift + i
3. Application -> local storage -> discordapp.com
4. Refresh (F5)
5. token string should now show up at the bottom of the local storage, copy it into `token.txt`

Example output:

![a](https://i.imgur.com/v6FsBIz.png)

[discord.py](https://github.com/Rapptz/discord.py)
