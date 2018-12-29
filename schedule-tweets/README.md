# Schedule tweets

When writing this document:
* There is no API for scheduling tweets into TweetDeck.
* There is an API for creating tweets, but I don't want to take care about the scheduling of that creation.
* There are tools to register user actions on a website, but I want to try another way :wink:

## Steps

1. Login into TweetDeck
2. Create a function into [Web Console](https://developer.mozilla.org/en-US/docs/Tools/Web_Console/The_command_line_interpreter) for creating a tweet (JQuery is not available). In this case, all the tweets will be scheduled at `10.30 AM`:
```
function createTweet(message, day, goToNextMonth) {
    $(".tweet-button").click();

    $(".js-compose-text").value = message;
    $(".js-compose-text").dispatchEvent(new InputEvent("change"));

    $(".js-schedule-button").click();
    $("#amPm").click();  // depends on the current time (default value)
    $("#scheduled-hour").value = 10;
    $("#scheduled-minute").value = 30;
    if (goToNextMonth) {
        $("#next-month").click();
    }
    $("a[href='#".concat(day).concat("']:not(.caldisabled):not(.caloff)")).click();

    $(".js-send-button").click();
}
```
3. Paste a list of calls to that function. For example, from 29th of December:
```
setTimeout(createTweet, 3000, '...', 30, 0);
setTimeout(createTweet, 6000, '...', 31, 0);
setTimeout(createTweet, 9000, '...', 1, 1);
setTimeout(createTweet, 12000, '...', 2, 0);
setTimeout(createTweet, 15000, '...', 3, 0);
setTimeout(createTweet, 18000, '...', 4, 0);
setTimeout(createTweet, 21000, '...', 5, 0);
setTimeout(createTweet, 24000, '...', 6, 0);
setTimeout(createTweet, 27000, '...', 7, 0);
setTimeout(createTweet, 30000, '...', 8, 0);
setTimeout(createTweet, 33000, '...', 9, 0);
setTimeout(createTweet, 36000, '...', 10, 0);
...
```
Imagine you have a file with a list of Twitter aliases which must be mentioned, calls could be created by: [calls-creation.py](calls-creation.py).
