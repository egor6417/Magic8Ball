# decider

import random

# write answers
ans1="Go for it!"
ans2="No way!"
ans3="I'm not sure. Ask me again."
ans4="Fear of the unknown is what imprisons us"
ans5="It would be madness to do that!"

print("shaking..\n" * 4)
# Get answer
choice=random.randint(1, 8)
if choice==1:
    answer=ans1
elif choice==2:
      answer=ans2
elif choice==3:
      answer=ans3
elif choice==4:
      answer=ans4
else:
      answer=ans5


print(answer)
    
input('\n\nTHANK YOU.')


