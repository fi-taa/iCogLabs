function flattenArray(arr) {
    if (!Array.isArray(arr)) {
        return [arr];
    }

    return arr.reduce((result, item) => {
        // console.log("result",result)
        // console.log("item",item)
        // console.log("flattening",flattenArray(item))
        return result.concat(flattenArray(item));
    }, []);
}


arr = [[4,[3]],[2,1]]

console.log("arr",arr)
console.log("flatten array",flattenArray(arr))