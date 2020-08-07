# MYSQL_BENCH_TEST


## 총 데이터 개수 약 133만 row

![image](https://user-images.githubusercontent.com/13353498/89622732-740b9480-d8ce-11ea-86c9-ebb5e32578fe.png)




## 초기 쿼리 
---

```
SELECT
  IP,
  SUM(COUNT)
FROM
  (
    SELECT
      src_ip as IP,
      COUNT(src_ip) as COUNT
    FROM
      basic_info
    WHERE
      proto != 'HTTP'
    GROUP BY src_ip
    UNION
    SELECT
      dst_ip as IP,
      COUNT(dst_ip) as COUNT
    FROM
      basic_info
    WHERE
      proto != 'HTTP'
    GROUP BY dst_ip
  )a
GROUP BY
  IP;

```

* 응답 결과 및 속도 
---
![image](https://user-images.githubusercontent.com/13353498/89623031-ee3c1900-d8ce-11ea-9cdf-c1b2ee57d935.png)

응답속도 약 0.940 ~ 1.0ms 


proto 컬럼을 varchar(20) -> INT로 변경 했을시 성능 개선됨 

응답속도 약 0.84  ~ 0.85 ms 로 0.1ms 개선
![image](https://user-images.githubusercontent.com/13353498/89624902-ecc02000-d8d1-11ea-83bb-1113b6a55890.png)


src_ip, dst_ip를 int로 변경하여 저장시 성능 개선
```
SELECT INET_ATON('120.120.120.120');
```

응답속도 약 0.77 ~ 0.8fh 0.3ms 개선

![image](https://user-images.githubusercontent.com/13353498/89625569-06ae3280-d8d3-11ea-952d-0e7d2c6fb3b2.png)






