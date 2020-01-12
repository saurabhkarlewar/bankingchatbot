## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot
- hallo
- heeey
- hi hi
- hey
- hey hey
- hello there
- hi
- hello
- yo
- hola
- hi?
- hey bot!
- hello friend

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- um thank you good bye
- okay cool uh good bye thank you
- okay thank you good bye
- you rock
- and thats all thank you and good bye
- thank you and good bye
- sorry about my mistakes thank you good bye
- noise thank you good bye
- thank you goodbye noise
- okay thank you goodbye
- uh thank you good bye
- thank you goodbye
- thank you goodbye noise thank you goodbye
- breath thank you goodbye
- thank you
- okay thank you
- thanks goodbye
- ah thank you goodbye
- thank you noise
- thank you good bye
- breath thank you very much goodbye
- thanks
- noise thank you goodbye
- unintelligible thank you goodbye
- uh okay thank you good bye
- thank you bye
- um okay thank you good bye

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- no new selection
- no thanks
- no thank you
- uh no
- breath no
- do you have something else
- no this does not work for me

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good
- correct

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- who are you?
- what are you?
- who made you?
- am I talking to a bot?
- am I talking to a human?
- what can you do?

## intent:stop
- ok then you cant help me
- that was shit, you're not helping
- you can't help me
- you can't help me with what i need
- i guess you can't help me then
- ok i guess you can't help me
- that's not what i want
- ok, but that doesnt help me
- this is leading to nothing
- this conversation is not really helpful
- you cannot help me with what I want
- I think you cant help me
- hm i don't think you can do what i want
- stop
- stop go back
- do you get anything?
- and you call yourself bot company? pff
- and that's it?
- nothing else?

## intent:thankyou
- um thank you good bye
- okay cool uh good bye thank you
- okay thank you good bye
- you rock
- and thats all thank you and good bye
- thank you and good bye
- sorry about my mistakes thank you good bye
- noise thank you good bye
- thank you goodbye noise
- okay thank you goodbye
- uh thank you good bye
- thank you goodbye
- thank you goodbye noise thank you goodbye
- breath thank you goodbye
- thank you
- okay thank you
- thanks goodbye
- ah thank you goodbye
- thank you noise
- thank you good bye
- breath thank you very much goodbye
- thanks
- noise thank you goodbye
- unintelligible thank you goodbye
- uh okay thank you good bye
- thank you bye
- um okay thank you good bye

## intent:chitchat
- can you share your boss with me?
- i want to get to know your owner
- i want to know the company which designed you
- i want to know the company which generated you
- i want to know the company which invented you
- i want to know who invented you
- May I ask who invented you?
- please tell me the company who created you
- please tell me who created you
- tell me more about your creators
- tell me more about your founders
- Ahoy matey how are you?
- are you alright
- are you having a good day
- Are you ok?
- are you okay
- Do you feel good?
- how are things going
- how are things with you?
- How are things?
- how are you
- how are you doing
- how are you doing this morning
- how are you feeling
- how are you today
- How are you?
- How is the weather today?
- What's the weather like?
- How is the weather?
- What is the weather at your place?
- Do you have good weather?
- Is it raining?
- What's it like out there?
- Is it hot or cold?
- Beautiful day, isn't it?
- What's the weather forecast?
- Is it quite breezy outside?

## intent:balance_check
- balance
- [savings](source_account) balance
- account balance
- balance in my account
<!-- - I want to know my [credit card](product) balance -->
- I want to know my [current](source_account) account balance
- I want to know my [current account](source_account:current)  balance
- I want to know my account balance
- I want to know my [savings](source_account) account balance
- I want to know my balance
- What is my [savings](source_account) account balance
- What is my account balance
- what is my balance 
- how much do I have on my [savings](source_account) 
- how much do I have on my [savings account](source_account:savings) 

## intent:transaction_details
- show me transaction details for [Dec](month)
- show me transaction details for [Oct](month)
- show me transaction details for [Nov](month)
- show me transaction details for [December](month)
- show me transaction details for [October](month)
- show me transaction details for [November](month)
- show me the transaction details
- transaction details for [Dec](month)
- transaction details for [Oct](month)
- transaction details for [Nov](month)
- transaction details for [December](month)
- transaction details for [October](month)
- transaction details for [November](month)

## intent:inform
- [savings](source_account)account
- [current](source_account) account
- [123457892](phoneno)
- [989479384](phoneno)
- My registerd mobile no is [989479384](phoneno)
- My registerd phone no is [989479384](phoneno)
- My rmn is [989479384](phoneno)
- My date of birth is [09061980](dob)
- My dob is [09061980](dob)
- DOB is [09061980](dob)

## regex:phoneno
- [0-9]{10}

## regex:dob
- [0-9]{8}

## lookup:source_account
- savings
- current

## intent:apply_for_new_product
- i want to apply for a new [credit](product) card
- i want to apply for a new [forex](product) card
- i want to apply for a new [debit](product) card
- i want to apply for a new [atm](product) card 
- new [credit](product) card
- new [forex](product) card
- new [atm](product) card
- i want to apply for new product
- new product

## lookup:product
- credit
- forex
- debit
- atm

## lookup:month
- Oct
- Nov
- Dec