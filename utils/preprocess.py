import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 42 feature columns + 1 label + 1 difficulty
columns = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land',
    'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised',
    'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells',
    'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login',
    'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
    'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
    'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
    'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label', 'difficulty'
]

def load_data(filepath):
    # Load the data with correct headers
    df = pd.read_csv(filepath, names=columns)

    # Drop the difficulty column
    df.drop('difficulty', axis=1, inplace=True)

    # Encode protocol_type, service, flag
    for col in ['protocol_type', 'service', 'flag']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    # Simplify label to 'normal' or 'attack'
    df['label'] = df['label'].apply(lambda x: 'normal' if x == 'normal' else 'attack')

    # Separate features and label
    X = df.drop('label', axis=1)
    y = df['label']
    
    return X, y
