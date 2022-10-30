import sys

lines = []
with open(sys.argv[1], "r") as f:
    while True:
        lin = f.readline()
        if lin == "":
            break;
        lin.strip()
        lines.append(lin)

mfile_rec = lines[0].split()

timing_events = []
note_events = []
t_max = 0

trk_cnt = 0
ln_cnt = 0
for line in lines:
    ln_cnt += 1
    words = line.split()

    if len(words) < 1:
        continue

    if words[0] == "MTrk":
        trk_cnt += 1

    if len(words) < 3:
        continue

    if words[1] == "Tempo":
        t = int(words[0])
        timing_events.append([[t, trk_cnt, ln_cnt], words])

    if words[1] == "Meta":
        if words[2] == "TrkEnd":
            t = int(words[0])
            if t > t_max:
                t_max = t

    if len(words) < 5:
        continue

    if words[1] == "TimeSig":
        t = int(words[0])
        timing_events.append([[t, trk_cnt, ln_cnt], words])

    if words[1] in ["On", "Off"]:
        t = int(words[0])
        if t > t_max:
            t_max = t
        note_events.append(
            [
                [t, trk_cnt, ln_cnt],
                [
                    str(t)
                    + " " + words[1]
                    + " ch=10 "
                    + words[3]
                    + " " + words[4]
                ]
            ]
        )

timing_events.sort()
note_events.sort()

new_meta_trkend_line = str(t_max) + " Meta TrkEnd"

print("MFile 1 3", mfile_rec[3])
print("MTrk")
for rec in timing_events:
    print(" ".join(rec[1]))
print(new_meta_trkend_line)
print("TrkEnd")
print("MTrk")
print(new_meta_trkend_line)
print("TrkEnd")
print("MTrk")
for rec in note_events:
    print(" ".join(rec[1]))
print(new_meta_trkend_line)
print("TrkEnd")

sys.exit(0)

for rec in note_events:
    print(rec)
