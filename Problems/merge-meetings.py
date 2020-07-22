# Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed
# ranges. A meeting is stored as a tuple ↴ of integers (start_time, end_time). These integers represent the number
# of 30-minute blocks past 9:00am.
#
# [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# [(0, 1), (3, 8), (9, 12)]
# Source - https://www.interviewcake.com/question/python3/merging-ranges

def merge_ranges(meetings):
    sorted_meetings = sorted(meetings)
    merged_meetings = [sorted_meetings[0]]

    for m_start, m_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if m_start <= last_merged_meeting_end:
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, m_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((m_start, m_end))

    return merged_meetings


x = [(0, 1), (3, 5), (4, 8)]
print(merge_ranges(x))

# O(nlog(n)) time and O(n) space
