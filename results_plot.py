f = open('responses_normal.txt')

success_count = 0
failed_count = 0
content = f.read().split(' ')
for word in content:
    if 'properly' in word:
        success_count += 1
    elif 'failed' in word:
        failed_count += 1
print("Success : " + str(success_count))
print("Failed : " + str(failed_count))
success_rate = (float(success_count)/1000) * 100
failed_rate = (float(failed_count)/1000) * 100
print("Success : " + str(success_rate) + ' %')
print("Failed : " + str(failed_rate) + ' %')