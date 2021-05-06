# File Load Function
def get_test_data(file_root)
    
    datas = Array.new
    f = File.open file_root,'r'
    
    while line = f.gets
        num_array = Array.new
        line.split.each do | num |
           num_array.push num.to_i 
        end
        datas.push num_array
    end

    return datas
end

# Main Function
def main(data)
    if data.length == 0
        return Array.new
    elsif data.length == 1
        return data
    end
    get_run data
end

# Timsort Subroutines
def get_run(data)
    runs = Array.new
    data_size = data.length

    idx_cur = 0
    while idx_cur < data_size
        sliced_data = data[idx_cur, 4]
        idx_cur += 4
        
        # 증가/감소 확인
        is_plus = true
        is_plus = false if sliced_data[1] - sliced_data[0] < 0
        
        # intersection sort
        sliced_data.each_with_index { |_, idx|
            if idx > 1
                cur = idx
                if is_plus == true
                    while cur > 0 and (sliced_data[cur] - sliced_data[cur-1] < 0)
                        # Swapping
                        tmp = sliced_data[cur]
                        sliced_data[cur] = sliced_data[cur-1]
                        sliced_data[cur-1] = tmp
                        cur -= 1
                    end
                else
                    if sliced_data[idx] > sliced_data[idx-1]
                        # Swapping
                        while cur > 0 and (sliced_data[cur] - sliced_data[cur-1] > 0)
                            tmp = sliced_data[cur]
                            sliced_data[cur] = sliced_data[cur-1]
                            sliced_data[cur-1] = tmp
                            cur -= 1
                        end
                    end
                end
            end
        }
        # 앞에 있는 원소들이 계속 증가 또는 감소하는 경우 이어붙이기

        if is_plus == true
            while idx_cur < data.size and data[idx_cur] - sliced_data[sliced_data.length - 1] >= 0
                sliced_data.push(data[idx_cur])
                idx_cur += 1
            end
        else
            while idx_cur < data.size and data[idx_cur] - sliced_data[sliced_data.length - 1] <= 0
                sliced_data.push(data[idx_cur])
                idx_cur += 1
            end
        end
        # 나머지 하나가 마지막 인덱스일 경우 합치기
        if idx_cur == data_size - 1
            sliced_data.each_with_index { |_, idx| 
                if is_plus == true and data[idx_cur] >= sliced_data[idx]
                    sliced_data.insert idx, data[idx_cur]
                    break
                elsif is_plus == false and data[idx_cur] <= sliced_data[idx]
                    sliced_data.insert idx, data[idx_cur]
                    break
                end
            }
            idx_cur = data_size
        end
        runs.push sliced_data
    end
    puts runs.inspect
    return runs
end



datas = get_test_data("test.txt")
datas.each do | data |
    main data
end

