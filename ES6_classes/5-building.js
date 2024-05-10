class Building {
  constructor(sqft) {
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  } // End constructor

  // Getter for sqft attribute
  get sqft() {
    return this._sqft;
  } // End getter for sqft attribute
}

export default Building;
