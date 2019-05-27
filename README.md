**README tiếng Việt ở dưới.**

# Investigate/Play with fasttext pretrained embeddings
Originally written to see how good the fasttext pretrained embeddings in Vietnamese are.

Can *probably* be used for other languages.

Output statements are in Vietnamese.

## Prerequisites
python 3+, with the following packages numpy, io, sys

pretrained word embedding .vec file, can be downloaded from https://fasttext.cc/docs/en/crawl-vectors.html or https://fasttext.cc/docs/en/pretrained-vectors.html

decent RAM, the more the better. Word vectors are very big.

## Usage
The embedding used in the examples is from https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.vi.300.vec.gz

### fasttext.py
Open the repo in the terminal

Run `python fasttext.py <embedding> <number of words to load>`

Example: `python fasttext.py cc.vi.300.vec 100000` will load up the first 100000 word vectors from `cc.vi.300.vec`

Type in a query word and press Enter to receive the 20 closest words to the query word, cosine-distance wise (the cosine distance is also shown).

Example:
```
Chọn một từ tiếng Việt, bấm Ctrl+C để thoát: đẹp
0.6155386803615271 	 tốt
0.6103087048078959 	 đẹp
0.5880328240342534 	 xinh
0.5701681769585834 	 Vẻ
0.5656049074918542 	 Đẹp
0.5585548603739252 	 xắn
0.5304753678843503 	 mới
0.5300792589061245 	 thật
0.5280522573172794 	 tuyệt
0.5210500510029121 	 rẻ
0.5091834661792562 	 trắng
0.5084583600312742 	 làm
0.5033618073435745 	 gái
0.501357762160667 	 hiền
0.49622119116504376 	 rất
0.4954064375755846 	 dáng
0.49392608508464364 	 sạch
0.4902017546999696 	 lộng
0.49006912989347623 	 vẻ
0.48957422105311194 	 đãng
```

### kingqueenman.py
Open the repo in the terminal

Run `python  <embedding> <number of words to load>`

Example:
`python fasttext.py cc.vi.300.vec 100000` will load up the first 100000 word vectors from `cc.vi.300.vec`

Select the 3 words one after another. The results shown will be v3+v2-v1.

Example:
```
Kết quả trả về là vector = nguồn_2 + (đích-nguồn)
bấm Ctrl+C để thoát
Chọn từ nguồn: nam
Chọn từ đích: nữ
Chọn từ nguồn_2: chồng
0.690544259444833 	 chồng
0.679583171175046 	 vợ
0.5729526096118742 	 Vợ
0.5645168720840441 	 bà
0.546199321158176 	 mẹ
0.515409502106918 	 cô
0.5108081749241871 	 nữ
0.48723665634831403 	 Bà
0.4514154554245706 	 goá
0.44980752728118983 	 Cô
0.44779389059646746 	 chị
0.44677735943587854 	 Chồng
0.4456833264850808 	 ôsin
0.43951249711592144 	 hờ
0.4309064759531058 	 mụ
0.4292090701213186 	 bồ
0.42843377206830063 	 Mẹ
0.42627474240900537 	 zợ
0.42310692755394813 	 ấy
0.4209171935864212 	 Nữ
```

# Khảo sát/Nghịch fasttext pretrained embeddings
Được viết để khảo sát chất lượng của mô hình fasttext tiếng Việt có sẵn. Có thể dùng để đọc fasttext của các ngôn ngữ khác.
## Yêu cầu
python 3+, với các thư viện numpy, io, sys

file pretrained word-embedding ```.vec```, tải từ https://fasttext.cc/docs/en/crawl-vectors.html hoặc https://fasttext.cc/docs/en/pretrained-vectors.html

RAM kha khá, càng nhiều càng tốt. Vector từ bự lắm.

## Usage
Mô hình embedding trong các ví dụ dưới đây được lấy từ https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.vi.300.vec.gz

### fasttext.py
Mở repo trong terminal

Chạy `python fasttext.py <embedding> <số từ muốn tải>`

Ví dụ `python fasttext.py cc.vi.300.vec 100000` sẽ tải 100000 vector từ trong `cc.vi.300.vec`

Nhập vào một từ hỏi bất kỳ và nhấn Enter để nhận về 20 từ gần nhất với từ hỏi, với khoảng cách cosine đính kèm.

Ví dụ:
```
Chọn một từ tiếng Việt, bấm Ctrl+C để thoát: đẹp
0.6155386803615271 	 tốt
0.6103087048078959 	 đẹp
0.5880328240342534 	 xinh
0.5701681769585834 	 Vẻ
0.5656049074918542 	 Đẹp
0.5585548603739252 	 xắn
0.5304753678843503 	 mới
0.5300792589061245 	 thật
0.5280522573172794 	 tuyệt
0.5210500510029121 	 rẻ
0.5091834661792562 	 trắng
0.5084583600312742 	 làm
0.5033618073435745 	 gái
0.501357762160667 	 hiền
0.49622119116504376 	 rất
0.4954064375755846 	 dáng
0.49392608508464364 	 sạch
0.4902017546999696 	 lộng
0.49006912989347623 	 vẻ
0.48957422105311194 	 đãng
```

### kingqueenman.py
Mở repo trong terminal

Chạy `python fasttext.py <embedding> <số từ muốn tải>`

Ví dụ `python fasttext.py cc.vi.300.vec 100000` sẽ tải 100000 vector từ trong `cc.vi.300.vec`

Chọn lần lượt 3 từ. Kết quả trả về là vector v3+v2-v1.
Ví dụ:
```
Kết quả trả về là vector = nguồn_2 + (đích-nguồn)
bấm Ctrl+C để thoát
Chọn từ nguồn: nam
Chọn từ đích: nữ
Chọn từ nguồn_2: chồng
0.690544259444833 	 chồng
0.679583171175046 	 vợ
0.5729526096118742 	 Vợ
0.5645168720840441 	 bà
0.546199321158176 	 mẹ
0.515409502106918 	 cô
0.5108081749241871 	 nữ
0.48723665634831403 	 Bà
0.4514154554245706 	 goá
0.44980752728118983 	 Cô
0.44779389059646746 	 chị
0.44677735943587854 	 Chồng
0.4456833264850808 	 ôsin
0.43951249711592144 	 hờ
0.4309064759531058 	 mụ
0.4292090701213186 	 bồ
0.42843377206830063 	 Mẹ
0.42627474240900537 	 zợ
0.42310692755394813 	 ấy
0.4209171935864212 	 Nữ
```
