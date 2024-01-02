class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        employee_access_times = defaultdict(list)
        
        for name, time in access_times:
            employee_access_times[name].append(int(time))
        print(employee_access_times)
        res = []
        for name, times in employee_access_times.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <100:
                    res.append(name)
                    break

        return res
        