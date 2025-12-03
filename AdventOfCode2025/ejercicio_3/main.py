from operator import indexOf
            
def firstStar():
    total: int = 0
    with open('input', 'r') as file:
        for line in file:
            nums = [int(i) for i in line[:-1]]
            greater: int = max(nums)
            new_nums = [i for i in nums[indexOf(line, str(max(nums))) + 1:]]
            if len(new_nums) > 0:
                lower: int = max(new_nums)
                total += (greater * 10) + lower
            else:
                new_nums = [i for i in nums[:indexOf(nums, greater)]]
                lower = greater
                greater = max(new_nums)
                total += (greater * 10) + lower
    print(total)

def secondStar():
    total = 0
    max_pines = 12

    with open('input', 'r') as file:
        for line in file:
            s = line.strip()
            if not s:
                continue

            n = len(s)
            keep = min(max_pines, n)
            k = n - keep
            stack = []
            for ch in s:
                while k > 0 and stack and stack[-1] < ch:
                    stack.pop()
                    k -= 1
                stack.append(ch)
            if k > 0:
                stack = stack[:-k]
            best_digits = stack[:keep]
            best_value = int("".join(best_digits))
            total += best_value
    print(total)
    
if __name__ == "__main__":
    firstStar()
    secondStar()