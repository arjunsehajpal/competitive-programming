class Solution:
    def findJudge(self, N: int, trust) -> int:
        audience = {i[0] for i in trust}
        audience_count = 0
        judge_candidate = -1

        for i in range(1, N+1):
            if i not in audience:
                judge_candidate = i

        for a, b in trust:
            del a
            if b == judge_candidate:
                audience_count += 1

        if audience_count != N - 1:
            judge_candidate = -1

        return judge_candidate