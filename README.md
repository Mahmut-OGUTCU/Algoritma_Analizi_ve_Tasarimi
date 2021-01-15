# Algoritma_Analizi_ve_Tasarimi
Çeşitli arama ve sıralama algoritmalarının 0 ile 100000 sayıları arasında (bucket sort algoritması dışında) kullanıcı girişli sayı kadar rastgele sayıların sıralanmasında ya da aranmasındaki geçen sürenin ve işlem sayısının Python programlama dili kullanılarak bulunması ve karşılaştırılması hedeflenmiştir.
Pythonda arayüz kütüphanesi olan tkinter modülü kullanılmış olup random sayı üretip daha kolay bir liste halinde tutabilmek için de numpy modülü kullanılmıştır. Tkinter modülü için herhangi bir ekleme yapılmadan kullanılabilirken, numpy modülü için;
 "pip install numpy"
şeklinde kullanılan IDE ye yazarak modülün kurulması gerekmektedir.
Arama algoritmaları olarak:

1.	Binary Search
2.	Linear Search

ve sıralama algoritmaları olarak:

1.	Bucket Sort
2.	Counting Sort
3.	Heap Sort
4.	Insertion Sort
5.	Merge Sort
6.	Quick Sort
7.	Radix Sort
algoritmaları kullanılmıştır.
Öncelikle program çalıştırıldığında iki buton seçenek olarak çıkar. İstediğimiz türe (Arama ya da Sıralama) göre bir seçim yaptıktan sonra karşımıza yukarıda belirtilen algoritmalar yine aynı şekilde karşımıza çıkar.
 
Eğer arama algoritmalarını kullanacaksak önümüze iki adet textbox çıkar ve birisi 0 ile 100000 arasında kaç sayı belirleneceği diğeri ise hangi sayıyı aratmak istediğimiz.

Arama algoritmaları değil de sıralama algoritmaları seçilmiş olsaydı karışımıza sadece bir adet textbox çıkardı ve bu da 0 ile 100000 arasında kaç sayı belirleneceği olurdu.

Bu değerlerin girdileri yapılıp algoritmalar başlatılır. Algoritmaların çalışması sonucunda:
Arama algoritmalarında:
1.	Bulunup bulunamama bilgisi,
2.	(bulunduysa indeks bilgisi),
3.	İşlem sayısı,
4.	Geçen süre
5.	ve programda kullanılan veri dizisi


Sıralama algoritmalarında:
1.	Sıralanmış veri dizisi,
2.	İşlem sayısı,
3.	Geçen süre
4.	ve sıralanmamış veri dizisi
kullanıcıya sunulur.

Arama Algoritmaları

Numpy kütüphanesi aracılığıyla 0 ile 100000 arasında kullanıcıdan girilen değer kadar sayı üretilip bir dizide tutulur. Pythonda .sort() methodu ile rastgele olan sayılar sıralanır.

1.	Binary Search

Daha sonra ortanca (son ve ilk indeksin ortasındaki tam indeks) bir değer bulunur ve alt değer (dizinin ilk indeksi) ile son değer (dizinin son indeksi) eşit oluncaya kadar üç sorgu gerçekleşir. Bu sorguların ilk maddesi gerçekleşmiyorsa aranan değer bulunamamıştır.

1-	Aranan sayı ortanca sayıya eşit mi?
Aranana sayıya eşitse arama başarılı ve değer bulunmuştur. Döngü kırılır.

2-	Aranan sayı ortanca sayıdan küçük mü?
Son değer ortanca-1 olur ve sorgu tekrarlar.

3-	Aranan sayı ortanca sayıdan büyük mü?
İlk değer ortanca+1 olur ve sorgu tekrarlar.

2.	Linear Search

Daha sonra ilk indeks’ten son indeks’e doğru bir döngü kurulur ve tek tek aranan değer sorgulanır. Bulunması halinde döngü kırılır.

Sıralama Algoritmaları

Numpy kütüphanesi aracılığıyla 0 ile 100000 (Bucket Sort dışında) arasında kullanıcıdan girilen değer kadar ratgele sayı üretilip bir dizide tutulur.

1.	Bucket Sort

0 ile 1 arasında kullanıcıdan girilen değer kadar rastgele sayı üretilip bir dizide tutulur. Daha sonrasında 10 adet kova oluşturulur ve 0.’dan sonra ilk basamağı aynı olanlar bir kovaya alınır ve elemanların hepsi yerleştikten sonra kovalar ayrı ayrı kendi içinde Insertion sort ile sıralanır. Son olarak da kovalar küçükten büyüğe şeklinde birleştirilir.

2.	Counting Sort

Daha sonrasında dizideki değerlerin aralık bilgilerini yeni bir dizi oluşturmak için kullanır. Oluşturulan yeni dizinin her bir satırı ana dizide o satır numarasının değerine sahip ögelerin sayısını gösterir. Yeni dizideki öge değeri sayıları daha sonra ana dizideki tüm değerlerin doğru konuma konulması için kullanılır.

3.	Heap Sort

Daha sonrasında kök eleman en büyük olacak şekilde bir ağaç yapısı oluşturulur. Yani bulunan kök düğümün çocukları kök düğümden küçük olur. Dizinin son elemanları dizinin ortasındaki elemanların çocuk düğümü olacağından bu işlem dizinin yarısına kadar yapılır. Elde edilen diziyi sıralamak için ise dizinin ilk elemanı en büyük olduğu bilindiğinde dizini son elemanıyla ilk elemanı yer değiştirilerek büyük eleman sona atılır. Bozulan diziye bu işlemler baştan sona tekrar uygulanır. Dizi boyutu 1 oluncaya kadar işleme devam edilir.

4.	Insertion Sort

Daha sonrasında ikinci indeksten son indekse bir döngü kurulur ve bulunduğu indeksten önceki indekslerle karşılaştırma yapılır (eğer büyük ise yer değiştir değilse olduğun indekste kal şeklinde). İndex sona ulaşınca sıralanmış dizimiz oluşur.

5.	Merge Sort

Daha sonrasnda veri dizisi sürekli sağ ve sol olmak üzere sürekli 2’ye bölünerek en küçük birime kadar ayrılır. Bu ayrılma sonrasında ayrımlar sıralanır. Sıralanma sonucu da en son olarak birleştirilir.

6.	Quick Sort

Daha sonrasında veri dizisinden bir pivot eleman seçilir (genelde son indeksten ilk indekse doğru) ve bu seçilen elemandan küçük olan tüm sayılar pivotun önüne büyük olanlar ise arkasına dizilir (Eşit olma durumunda programcının yazımına göre ister önüne ister arkasına dizilir). Daha sonrasında recursive olarak bu işlemler tekrar eder ve pivot ilk elemana eşit olunca sıralama tamamlanmıştır.

7.	Radix Sort

Daha sonrasında birler, onlar, yüzler... basamağı şeklinde basamak basamak sıralar. (XYZ olarak üç basamaklı bir sayı olarak düşünürsek öncelikli olarak en sağda bulunan birler basamağı (Z sırası) sıralanır. Sıralama bittikten sonra onlar basamağı ve birler basamağı (YZ sırası) sıralanır. Z sırası zaten sıralı olduğu için Y’ler karşılaştıralarak gider.)
