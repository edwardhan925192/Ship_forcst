# Setting  
```markdown
!unzip /content/drive/MyDrive/data/hyundai/hyundai.zip  
!git clone https://github.com/edwardhan925192/Ship_forcst.git  
%cd /content/Ship_forcst  
```

# Ship_forecast  
```markdown
!python main.py\
--lists ARI_CO SHIP_TYPE_CATEGORY\
--file_path1 '/content/Ship_forcst/train.csv' \
--file_path2 '/content/Ship_forcst/test.csv' \
--load \
--preprocess \
--extract_dates \
--datetime_col 'ATA'

```

preprocess deletes dist with 0  
extract_date converts dates into year,month, and so on.  


# Submission  
```markdown
from submission import get_submission  
get_submission(pred_path, test_path, name)  
```

# Chuseok  
```markdown
#Initialize
import pandas as pd
!unzip '/content/drive/MyDrive/data/chuseok.zip'
train = pd.read_csv('/content/train.csv')
test = pd.read_csv('/content/test.csv')

#Functions
chuseok.py

#Submission  
direct_submission(test_predictions,'/content/test.csv',result11)
```
