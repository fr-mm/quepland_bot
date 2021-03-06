A simple library for recording and playing mouse macros at regular intervals between clicks.

# Compatibility

Built and tested on Ubuntu 21.04. 

# Installation

```
pip install quepland_bot
```

# Usage
Import and instantiate QueplandBot

```
from quepland_bot import QueplandBot


bot = QueplandBot()
```

Record clicks: once the method is called, it will wait for a space bar press to begin recording.
Press any kay to stop recording.
```
bot.record_clicks()
```

Play what you recorded until any key is pressed:
```
bot.run()
```


## Changing intervals between clicks

When instantiating QueplandBot you can define how many seconds it will take between clicks when playing a sequence.
Default is 0.1 seconds.

```
bot = Queplandbot(default_seconds_between_clicks=0.5)
```

## Saving routines

You can save a sequence of clicks by assigning the return of `record_clicks()` to a variable.
To play it, pass it as an argument to `run()`. 
When `run()` is called without arguments it runs last routine recorded.

```

bot = QueplandBot()

one_routine = bot.record_clicks()
other_routine = bot.record_clicks()

bot.run(one_routine)

```