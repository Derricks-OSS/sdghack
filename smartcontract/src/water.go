package main

import (
	"strconv"

	"github.com/orbs-network/orbs-contract-sdk/go/sdk/v1"
	"github.com/orbs-network/orbs-contract-sdk/go/sdk/v1/state"
)

var PUBLIC = sdk.Export(addOil, getOil, addWater, getWater, registerTenantWithOwner, getTenantsForOwner)
var SYSTEM = sdk.Export(_init)

var BALANCE_OIL_KEY = []byte("balance.oil")
var BALANCE_WATER_KEY = []byte("balance.water")

func _init() {
	//tenantsByOwner := map[string]string{}
}

func addOil(owner []byte, month uint32, year uint32, amount uint64) {
	state.WriteUint64(getKey(BALANCE_OIL_KEY, owner, month, year), amount)
	/*
		Compare amount to amount for preceding year. If less, distribute 70% of the difference equally to 
		all tenants for that owner.
	*/
}

func getOil(owner []byte, month uint32, year uint32) uint64 {
	return state.ReadUint64(getKey(BALANCE_OIL_KEY, owner, month, year))
}

func addWater(owner []byte, month uint32, year uint32, amount uint64) {
	state.WriteUint64(getKey(BALANCE_WATER_KEY, owner, month, year), amount)
	/*
		Compare amount to amount for preceding year. If less, distribute 70% of the difference equally to 
		all tenants for that owner.
	*/
}

func getWater(owner []byte, month uint32, year uint32) uint64 {
	return state.ReadUint64(getKey(BALANCE_WATER_KEY, owner, month, year))
}

func getKey(keyName []byte, owner []byte, month uint32, year uint32) []byte {
	return append(append(append(keyName, owner...), strconv.Itoa(int(month))...),
		strconv.Itoa(int(year))...)
}

func registerTenantWithOwner(owner []byte, tenant []byte) {
	//tenantsByOwner[string(owner)] = string(tenant)
}

func getTenantsForOwner(owner []byte) string {
	return "tenant"
	//return tenantsByOwner[string(owner)]
}
