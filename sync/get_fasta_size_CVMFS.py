import yaml
with open("sync/cvmfs_20260715_fasta_only/all_fasta.yaml", 'r') as f:
    all_fasta_content = yaml.safe_load(f)

total_size = 0
for entry in all_fasta_content['all_fasta']:
    path = entry['path']
    fasta_file = path.split('/')[-1]
    found = False
    for file in entry['manifest']:
        if file['path'] == fasta_file:
            found = True
            total_size += file['size']
    if not found:
        print("Could not find fasta file for")
        print(entry)

print("Total size of fasta files is:")
print(total_size)
print(f"{round(total_size / 1024**3, 2)}GB")
