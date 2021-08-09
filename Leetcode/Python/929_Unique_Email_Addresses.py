"""
929. Unique Email Addresses

Difficulty:- Easy

https://leetcode.com/problems/unique-email-addresses/
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
author:- aarifsk
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = 0
        dicts ={}
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".","")
            if local+domain not in dicts.keys():
                dicts[local+"@" + domain] = 1
            else:
                dicts[local+"@" + domain] += 1
        return len(dicts.keys())
