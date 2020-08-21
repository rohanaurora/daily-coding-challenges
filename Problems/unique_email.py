class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for e in emails:
            name, domain = e.split('@')
            name = (name.split('+'))[0]
            name = name.replace('.', '')
            s.add(name+'@'+domain)
        return len(s)