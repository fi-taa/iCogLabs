

const curriedVolume = (height) => { return (width) => { return (length) => {return height*length*width} }; };

const Volume = curriedVolume(10);

console.log(Volume)